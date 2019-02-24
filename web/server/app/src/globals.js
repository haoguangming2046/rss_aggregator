import axios from 'axios';
import Cookie from 'js-cookie';

const csrftoken = Cookie.get('csrftoken');

axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.headers['X-CSRFToken'] = csrftoken;
axios.defaults.headers['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.headers['Content-Type'] = 'application/json';

export default axios;
