const axios = require('axios');
axios.get('https://api.github.com/users/octocat')
 .then(res => console.log('User:', res.data.login))
 .catch(err => console.error(err));
