const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
	//console.log('Online at\n-----' + D.toString().replace('UTC','CDT').replace('+0000','-0500') + '\n-----' + UTC);
	client.user.setActivity('type s~help for commands');
	// Check for the various File API support.
	if (window.File && window.FileReader && window.FileList && window.Blob) {
		readSingleFile();
	} else {
		console.log('The File APIs are not fully supported by your browser.');
	}
});

client.on('message', message => {
	message.content = message.content.toLowerCase()
	if (message.content.substring(0,2) === 's~' && message.author.bot == false) {
		var args = message.content.substring(2).split(' ');
		var cmd = args[0];
		args = args.splice(1).toString().replace(/,/g,' ');
    		if(cmd == 'ping'){
    			message.reply('pong');
			document.getElementById("test").innerHTML = message.content;
		}
	}
});

function readSingleFile(evt) {
	//Retrieve the first (and only!) File from the FileList object
	var f = evt.target.files[0]; 

	if (f) {
		var r = new FileReader();
		r.onload = function(e) { 
			var contents = e.target.result;
			console.log( "Got the file.n" +"name: " + f.name + "n"+"type: " + f.type + "n" +"size: " + f.size + " bytesn"  + "starts with: " + contents.substr(1, contents.indexOf("n")));  
		}
		r.readAsText(f);
	} else { 
		console.log("Failed to load file");
	}
}

//document.getElementById('fileinput').addEventListener('change', readSingleFile, false);

client.login(process.env.BOT_TOKEN);
