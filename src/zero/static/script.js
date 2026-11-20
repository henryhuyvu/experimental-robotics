let currentCommand = 'S';

function sendCommand(cmd) {
    if (cmd === currentCommand && cmd !== 'S') return; // Prevent spamming the same command
    currentCommand = cmd;
    
    fetch('/command', {
        method: 'POST',
        body: cmd
    }).catch(err => console.error('Error sending command:', err));
}

// Keyboard event listeners
document.addEventListener('keydown', (event) => {
    switch(event.key.toLowerCase()) {
        case 'w': sendCommand('F'); break;
        case 's': sendCommand('B'); break;
        case 'a': sendCommand('L'); break;
        case 'd': sendCommand('R'); break;
        case ' ': sendCommand('S'); break;
    }
});

document.addEventListener('keyup', (event) => {
    const keys = ['w', 's', 'a', 'd'];
    if (keys.includes(event.key.toLowerCase())) {
        sendCommand('S'); // Stop when key is released
    }
});
