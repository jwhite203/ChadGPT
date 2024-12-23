// Simple AI logic
const responses = [
    { keyword: "hello", response: "Hi there! How can I assist you today?" },
    { keyword: "bye", response: "Goodbye! Have a great day!" },
    { keyword: "help", response: "Sure! What do you need help with?" },
    { keyword: "weather", response: "I'm not sure about the weather, but I hope it's sunny!" },
];

function simpleAI(input) {
    // Convert user input to lowercase for matching
    const lowerInput = input.toLowerCase();

    // Check if the input matches any keyword
    for (const pair of responses) {
        if (lowerInput.includes(pair.keyword)) {
            return pair.response;
        }
    }

    // Default response if no keyword matches
    return "I'm not sure how to respond to that.";
}

// Test the AI
const userInput = "Can you tell me about the weather?";
const botResponse = simpleAI(userInput);
console.log("Bot says:", botResponse);
