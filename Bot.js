/*const { Client, Intents } = require('discord.js');
    require("dotenv").config();
    const client = new Client({intents:[Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });                                         
    const mySecret = process.env['DISCORD_BOT_TOKEN'];
     client.on("ready", () => {
     console.log(`Logged is as ${client.user.tag}!`);
    });


   client.on("message", (msg) => {
    if(msg.content === "ping"){
    msg.reply("pong");
   }
   });

   client.login(mySecret);
*/

   // Posting GIFs
// Discord Bots
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/learning/bots/discord/05-posting-gifs.html
// https://youtu.be/Q6nWCGUVC6s

console.log('Hello');

const fetch = import("node-fetch");

const { Client, Intents } = require('discord.js');
    require("dotenv").config();
    const client = new Client({intents:[Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.login(process.env.DISCORD_BOT_TOKEN);

client.on('ready', readyDiscord);

function readyDiscord() {
  console.log('💖');
}

const replies = [
  '🚂🌈💖',
  'I love you too!',
  "Bitch, you’re my soulmate",
  'Bitch you better be joking'
]

client.on('message', gotMessage);

async function gotMessage(msg) {
  // if (msg.channel.id == "715786219770085396") {
  // use cleanContent instead of content to remove tagging
  let tokens = msg.cleanContent.split(" ");
  const fetch = (await import('node-fetch')).default

  if (tokens[0] === "!loveYou") {
    const index = Math.floor(Math.random() * replies.length);
    msg.channel.send(replies[index]);
  } else if (tokens[0] == "!gif") {
    let keywords = "euphoria";
    if (tokens.length > 1) {
      keywords = tokens.slice(1, tokens.length).join(" ");
    }
    let url = `https://api.tenor.com/v1/search?q=${keywords}&key=${process.env.TENORKEY}&contentfilter=high`;
    let response = await fetch(url);
    let json = await response.json();
    const index = Math.floor(Math.random() * json.results.length);
    msg.channel.send(json.results[index].url);
    msg.channel.send("GIF from Tenor: " + keywords);
  }

}