<template>
<div class="pure-g">
    <div v-for="item in gridData" class="pure-u-1-5">
        <div class="padded">
            <div class="image" :style="'background-image: url(img/' + item.filename + ')'">
                <img :src="placeholder" class="pure-img">
            </div>
        </div>
    </div>
</div>
</template>

<script>
var empty = require('../assets/d.png');
module.exports = {
    name: 'grid-component',
    props: ['gridData'],
    data: function controller() {
        return {
            placeholder: empty
        };
    },
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
