var empty = require('../assets/d.png');
module.exports = {
    name: 'grid-component',
    props: ['gridData', 'defaultMonth'],
    data: function controller() {
        return {
            placeholder: empty
        };
    },
    computed: {
        Grid: function grid() {
            if (typeof this.gridData !== 'undefined' && this.gridData !== null) {
                var f = this.$root.currentRoute.replace('#/', '');
                if (f === '') {
                    f = this.defaultMonth;
                }
                return this.gridData.filter(function filter(item) {
                    return item.date.indexOf(f) !== -1;
                });
            }
            return [];
        }
    }
};
