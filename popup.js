document.getElementById('sendUrl').addEventListener('click', function (){
    const url = document.getElementById('urlInput').value;
    chrome.runtime.sendNativeMessage('com.example.native', {url}, (response) => {
        console.log('Received response from native host: ', response)
    });
});