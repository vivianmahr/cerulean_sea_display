var reply_controller = c_sea_app.controller("replyController", function($scope, $http){
	$scope.isText= true;
	$scope.tokens = [];
	$scope.selected_token = -1;
	$scope.textContents = ["Hello! My name is Kyte from Cerulean Sea. I am a program who will try to analyze your sentence and answer from a list of replies. Here are my instructions",
	"1) Please use proper grammar and spelling with me! I am a young bot who hasn't learned how to autocorrect yet. ",
	"2) Only send in one sentence at a time.",
	'3) I have learned some special commands. If you are interested, ask about "special commands" or try asking who my creator is.'];
	$scope.sentence = "";
	$scope.sendSentence = function (event) {
        if(event.which === 13) {
        	   $http({
			      method: 'GET',
			      url: 'process_sentence/',
			      params: {"data": $scope.sentence}
			   }).then(function (response){
			   		$scope.isText = response.isText;
			   		$scope.textContents = response.data.text;
			   		$scope.tokens = response.data.tokens;
			   },function (error){
			   		$scope.isText = true;
			   		$scope.textContents = ["Er... Something went wrong. Perhaps wait a while to try again. "]
			   });
			$scope.sentence="";
    	}
    };
    $scope.update_info_div = function(event, token) {
    	$scope.selected_token = token;
    }
});

reply_controller.directive('replyTable', function() { 
  return { 
    templateUrl: "static/directives/replyTable.html"
  }; 
});

reply_controller.directive('explanation', function() { 
  return { 
    templateUrl: "static/directives/explanation.html"
  }; 
});
