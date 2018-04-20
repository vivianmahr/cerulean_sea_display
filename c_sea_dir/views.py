from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import sentence_processing
import json
import spacy

nlp = spacy.load('en')
def to_token_dict(token):
	result = {
		"original": token.text,
		"lemma": token.lemma_,
		"pos": token.pos_,
		"shape": token.shape_,
		"isStop": token.is_stop
	}
	return result
	
# Create your views here.
def index(request):
    return render(request, "index.html")

def process_sentence(request):
	sentence = request.GET["data"]
	is_text = False
	tokens = []
	text = []

	special = sentence_processing.is_special_case(sentence.lower())

	if not (special[0]):
		nlp_sent = nlp(sentence)
		is_text = False
		tokens = [to_token_dict(t) for t in nlp_sent]
		text = []
	else:
		is_text = True
		tokens = []
		text = special[1].split("\n")
	return JsonResponse({
		"isText" : is_text,
		"tokens" : tokens,
		"text" : text
		})


