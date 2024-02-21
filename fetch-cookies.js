const fetch = require('node-fetch');
const fs = require('fs');

const url = 'https://thetvapp.to/';

(async () => {
    try {
        const response = await fetch(url);
        
        if (response.ok) {
            const headers = response.headers;
            const setCookieHeaders = headers.raw()['set-cookie'];
            
            // Write cookies to a file
            fs.writeFileSync('cookies.json', JSON.stringify({ cookies: setCookieHeaders }));
            
            console.log('Cookies fetched and saved successfully.');
        } else {
            console.error('Request failed with status', response.status);
        }
    } catch (error) {
        console.error('Error fetching cookies:', error);
    }
})();
