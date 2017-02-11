<template>
<div class="pure-g" v-if="item">
    <div class="pure-u-1-2">
        <div class="padded">
            <div class="image" :style="'background-image: url(' + item['img-source'] + ')'">
                <img :src="placeholder" class="pure-img"></a>
            </div>
        </div>
        <a class="pure-button" style="float:left" :href="item.previousUrl" v-if="item.previousUrl">&lt;</a>
        <a class="pure-button" style="float:right" :href="item.nextUrl" v-if="item.nextUrl">&gt;</a>
    </div>
    <div class="pure-u-1-2">
        <div class="info">{{item.displayDate}} <div class="divider"></div> &#9829; {{item.likes}}</div>
        <div class="info" v-html="item.text"></div>
        <div class="info" v-if="item.comments.length > 0">
            <div class="comment-block">
                <div class="comment" v-for="c in item.comments">
                    <b>{{c.author}}</b> {{c.text}}
                </div>
            </div>
        </div>
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

    .divider {
        display: inline-block;
        width: 3em;
    }

    .info {
        padding: 1em;
        padding-top: 0;
        white-space: pre-line;
    }

    .comment-block {
        border-top: 1px solid #666666;
        padding-top: 1em;
    }

    .comment {
        font-size: 0.9em;
        color: #666666;
    }

    .image {
        background-position-x: 50%;
        background-position-y: 50%;
        background-repeat: no-repeat;
        background-size: contain;
    }
</style>

<style>
    .hashtag {
        color: #CCCCCC;
    }
</style>
