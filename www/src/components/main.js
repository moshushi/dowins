var Menu = require('./menu.vue');
var Grid = require('./grid.vue');
var Cell = require('./cell.vue');

var main = {
    name: 'main',
    props: ['instagram', 'monthId', 'cellId'],
    data: function controller() {
        return {
            username: 'test'
        };
    },
    components: {
        'menu-component': Menu,
        'grid-component': Grid,
        'cell-component': Cell
    },
    computed: {
        route: function route() {
            if (typeof this.instagram === 'undefined' || this.instagram === null) {
                return ''; // data is not loaded yet
            }
            var f = this.$root.currentRoute.replace('#/', '');
            var url = f.split('/');
            if (url.length === 1 && url[0] !== '') {
                this.monthId = url[0];
                return 'grid';
            } else if (url.length > 1) {
                this.cellId = url[1];
                return 'cell';
            }
            this.monthId = this.instagram.defaultMonth;
            return 'grid'; // default component
        }
    }
};

module.exports = main;
