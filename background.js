console.log("Background script is running.");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    chrome.runtime.sendNativeMessage('com.example.native', message, (response) => {
        console.log('Received response from native host:', response);
    });
});