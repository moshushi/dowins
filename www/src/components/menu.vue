<template>
<div class="pure-menu custom-restricted-width">
    <div v-for="item in menuData">
        <span class="pure-menu-heading" >{{ item.year }}</span>

        <ul class="pure-menu-list">
            <li v-for="m in item.items" class="pure-menu-item" v-bind:class="{ 'pure-menu-selected': m.id === monthId }">
                <a :href="m.url" class="pure-menu-link">{{ m.name }}</a>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
module.exports = {
    name: 'menu-component',
    props: ['menuData', 'monthId']
};
</script>

<style></style>
