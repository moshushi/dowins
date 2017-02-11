<template>
<div class="pure-g" v-if="item">
    <div class="pure-u-3-5">
        <div class="padded">
            <div class="image" :style="'background-image: url(' + item['img-source'] + ')'">
                <img :src="placeholder" class="pure-img"></a>
            </div>
        </div>
    </div>
    <div class="pure-u-2-5">
        <div>{{item.date}}</div>
        <div>{{item.text}}</div>
        <div>{{item.likes}}</div>
    </div>
</div>
</template>

<script>
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
                    function fn(item) {
                        return item.id === self.cellId;
                    }
                )[0];
            }
            return null;
        }
    }
};
</script>

<style scoped>
    .padded {
        padding: 1px;
    }

    .image {
        background-position-x: 50%;
        background-position-y: 50%;
        background-repeat: no-repeat;
        background-size: cover;
    }
</style>
