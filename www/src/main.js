require('purecss/build/pure.css');
require('purecss/build/grids-responsive.css');

var Vue = require('vue');
var main = require('./components/main.vue');

var v = new Vue({
    el: '#app',
    render: function render(handler) {
        return handler(main);
    }
});
