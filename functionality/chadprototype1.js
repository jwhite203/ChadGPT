const { Client, GatewayIntentBits } = require('discord.js');
const axios = require('axios');

const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

const OPENAI_API_KEY = 'your-openai-api-key';

client.once('ready', () => {
    console.log('Bot is online!');
});

client.on('messageCreate', async (message) => {
    if (message.author.bot) return;

    const prompt = `You are an AI assistant. Respond to: "${message.content}"`;

    try {
        const response = await axios.post('https://api.openai.com/v1/completions', {
            model: 'text-davinci-003',
            prompt: prompt,
            max_tokens: 150,
        }, {
            headers: {
                'Authorization': `Bearer ${OPENAI_API_KEY}`,
                'Content-Type': 'application/json',
            }
        });

        const aiResponse = response.data.choices[0].text.trim();
        message.reply(aiResponse);
    } catch (error) {
        console.error('Error:', error);
        message.reply('Sorry, I encountered an error while trying to respond.');
    }
});

client.login('your-bot-token');
