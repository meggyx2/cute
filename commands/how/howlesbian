const lib = require("../../lib/lib.js");

module.exports.run = (bot, guild, message, args) => {
    var user = message.mentions.users.first() || message.author;

    return message.channel.send(`<@${user.id}> is ${lib.randomPercent()} lesbian!`);
}
