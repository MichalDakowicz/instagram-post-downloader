document.addEventListener('DOMContentLoaded', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      var pageUrl = tabs[0].url;
  
      // Copy page link to clipboard
      var copyText = document.createElement('textarea');
      copyText.value = pageUrl;
      document.body.appendChild(copyText);
      copyText.select();
      document.execCommand('copy');
      document.body.removeChild(copyText);
  
      // Notify the user that the link has been copied
      var notification = document.createElement('div');
      notification.textContent = 'Page link copied to clipboard!';
      notification.className = 'notification';
      document.body.appendChild(notification);
  
      // Remove the notification after a short delay
      setTimeout(function() {
        document.body.removeChild(notification);
      }, 2000);
    });
  });
  