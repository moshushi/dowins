module.exports = {
    makeUrl: function makeUrl(monthId, itemId) {
        if (itemId) {
            return '#/' + monthId + '/' + itemId;
        }
        return '#/' + monthId;
    }
};
