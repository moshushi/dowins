<template>
    <div>
        <div class="pure-g">
            <div class="pure-u-1">
                <h1>Instagram: @{{username}}</h1>
            </div>
        </div>
        <div class="pure-g">
            <div class="pure-u-1-5">
                <menu-component :menuData="instagram.menuItems"/>
            </div>
            <div class="pure-u-3-5">
                {{ instagram[0] }}
            </div>
        </div>

    </div>
</template>

<script>
var Menu = require('./menu.vue');
    
var main = {
    name: 'main',
    props: ['instagram'],
    data: function controller() {
        return {
            username: 'test'
        };
    },
    components: {
        'menu-component': Menu
    }
};

module.exports = main;
</script>

<style></style>
