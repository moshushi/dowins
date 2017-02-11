var empty = require('../assets/d.png');
module.exports = {
    name: 'grid-component',
    props: ['gridData', 'monthId'],
    data: function controller() {
        return {
            placeholder: empty
        };
    },
    computed: {
        Grid: function grid() {
            var monthId = this.monthId;
            if (typeof this.gridData !== 'undefined' && this.gridData !== null) {
                return this.gridData.filter(function filter(item) {
                    return item.date.indexOf(monthId) !== -1;
                });
            }
            return [];
        }
    }
};
