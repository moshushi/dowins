<template>
    <div>
        <div class="pure-g">
            <div class="pure-u-1">
                <h1>Instagram: @{{username}}</h1>
            </div>
        </div>
        <div class="pure-g">
            <div class="pure-u-1-5">
                <menu-component :menuData="instagram.menuItems" :monthId="monthId"/>
            </div>
            <div class="pure-u-4-5">
                <grid-component v-if="route === 'grid'" :gridData="instagram.images" :monthId="monthId"/>
                <cell-component v-if="route === 'cell'" :cellData="instagram.images" :cellId="cellId" />
            </div>
        </div>

    </div>
</template>

<script src="./main.js"></script>

<style></style>
