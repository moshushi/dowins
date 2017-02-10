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
            <div class="pure-u-4-5">
                <grid-component v-if="route === 'grid'" :gridData="instagram.images" :defaultMonth="instagram.defaultMonth"/>
                <cell-component v-if="route === 'cell'" :cellData="instagram.images" :cellId="cellId" />
            </div>
        </div>

    </div>
</template>

<script>
var Menu = require('./menu.vue');
var Grid = require('./grid.vue');
var Cell = require('./cell.vue');
    
var main = {
    name: 'main',
    props: ['instagram', 'cellId'],
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
            var f = this.$root.currentRoute.replace('#/', '');
            var r = f.split('/');

            if (r.length > 1) {
                this.cellId = r[1];
                return 'cell';
            }
            return 'grid'; // default component
        }
    }
};

module.exports = main;
</script>

<style></style>
