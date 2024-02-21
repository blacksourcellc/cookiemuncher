const express = require('express');
const fetch = require('node-fetch');
const fs = require('fs');

const url = 'https://thetvapp.to/';
const app = express();
const PORT = 3000;

app.get('/get-cookies', async (req, res) => {
    try {
        const response = await fetch(url);

        if (response.ok) {
            const headers = response.headers;
            const setCookieHeaders = headers.raw()['set-cookie'];

            // Write cookies to a file
            fs.writeFileSync('cookies.json', JSON.stringify({ cookies: setCookieHeaders }));

            res.json({ cookies: setCookieHeaders });
        } else {
            console.error('Request failed with status', response.status);
            res.status(response.status).json({ error: 'Request failed' });
        }
    } catch (error) {
        console.error('Error fetching data:', error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
