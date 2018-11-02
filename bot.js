const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
	console.log(`Logged in as ${client.user.tag}!`);
	//console.log('Online at\n-----' + D.toString().replace('UTC','CDT').replace('+0000','-0500') + '\n-----' + UTC);
	client.user.setActivity('type s~help for commands');
});

client.on('message', message => {
	message.content = message.content.toLowerCase()
	if (message.content.substring(0,2) === 's~' && message.author.bot == false) {
		var args = message.content.substring(2).split(' ');
		var cmd = args[0];
		args = args.splice(1).toString().replace(/,/g,' ');
    		if(cmd == 'ping'){
    			message.reply('pong');
			document.createElement("p").innerHTML = message.content;
		}
	}
});

client.login(process.env.BOT_TOKEN);
