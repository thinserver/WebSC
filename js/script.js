// tabs to the left!
$(function() {
	$( "#tabs" ).tabs().addClass( "ui-tabs-vertical ui-helper-clearfix" );
	$( "#tabs li" ).removeClass( "ui-corner-top" ).addClass( "ui-corner-left" );


	// Jquery Drag and Drop to Upload function
	var queueItemTemplate = '<div class="item"><div class="fileName">-</div><div class="progressBar"><div class="progress"></div></div></div>';

	var dropUpload = $('.dropUpload');
	var dropArea = dropUpload.find('.dropArea');

	var queue = dropUpload.find('.queue');
	var messages = dropUpload.find('.messages');
	var form = dropUpload.parent('form');

	dropArea.dropUpload({
		'url': form.attr('action'),
		'fileMeta': function(){
			var meta = {};
			$.each(form.serializeArray(), function(i) {
				meta[this.name] = this.value;
			});
			return meta; // Attach form data to each dropped file
		},
		'fileParamName': 'file',
		'fileSizeMax': null,
		'onDragEnter': function(){
			dropArea.addClass('isHovering');
		},
		'onDragLeave': function(){
			dropArea.removeClass('isHovering');
		},
		'onDropSuccess': function(){
			messages.html(''); // Empties message area at drop
			dropArea.removeClass('isHovering');
		},
		'onProgressUpdated': function(File, progress){
			File.queueItem.find('.progress').css('width', (progress * 100) + '%');
		},
		'onFileCompleted': function(File){
			File.queueItem.remove(); // Removed DOM queue item on completion
		},
		'onFileQueued': function(File){ // Created DOM queue item and attaches it to the File object
			var qi = $(queueItemTemplate);
			qi.find('.fileName').html(File.name);
			qi.appendTo(queue);
			File.queueItem = qi;
		},
		'onFileSucceeded': function(File, response){
			messages.text(response);
		},
		'onQueueCompleted': function(){
			alert("All done");
		}
	});

});