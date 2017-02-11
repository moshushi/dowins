var empty = require('../assets/d.png');

module.exports = {
    name: 'cell-component',
    props: ['cellData', 'cellId'],
    data: function controller() {
        return {
            placeholder: empty
        };
    },
    computed: {
        item: function item() {
            var self = this;
            if (typeof self.cellData !== 'undefined' && self.cellData !== null) {
                return self.cellData.filter(
                    function fn(arrItem) {
                        return arrItem.id === self.cellId;
                    }
                )[0];
            }
            return null;
        }
    }
};
