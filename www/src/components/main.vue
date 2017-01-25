<template>
    <div>
        <div class="pure-g">
            <div class="pure-u-1">
                <h1>Instagram: @{{username}}</h1>
            </div>
        </div>
        <div class="pure-g">
            <div class="pure-u-1-5">
                <menu-component/>
            </div>
            <div class="pure-u-3-5">
                ...
            </div>
        </div>

    </div>
</template>

<script>
var Menu = require('./menu.vue');
console.log(Menu);

module.exports = {
    name: 'main',
    data: function controller() {
        return {
            username: 'test'
        };
    },
    components: {
        'menu-component': Menu
    }
};
</script>

<style></style>
