<template>
<div class="pure-menu custom-restricted-width">
    <div v-for="item in menuData">
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
    props: ['menuData']
};
</script>

<style></style>
