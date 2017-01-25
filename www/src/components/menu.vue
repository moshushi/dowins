<template>
<div class="pure-menu custom-restricted-width">

    <div v-for="item in data">
        <span class="pure-menu-heading" >{{ item.year }}</span>

        <ul class="pure-menu-list">
            <li class="pure-menu-item" v-for="m in item.items">
                <a v-bind:href="'#/' + m.id" class="pure-menu-link">{{ m.name }}</a>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
module.exports = {
    name: 'menu-component',
    data: function controller() {
        return {
            data: [
                {
                    year: 2016,
                    items: [
                        {name: 'January', id: '2016-01'},
                        {name: 'February', id: '2016-02'}
                    ],
                },
                {
                    year: 2017,
                    items: [
                        {name: 'January', id: '2015-01'},
                        {name: 'February', id: '2015-02'}
                    ],
                }
            ]
        };
    }
};
</script>

<style></style>
