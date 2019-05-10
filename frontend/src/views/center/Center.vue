<template>
    <div class="center-wrap">
        <Aside :screenWidth="screenWidth"
               @changeCenterPadding="changeCenterPadding"></Aside>
        <div class="center" :style="centerPadding" v-if="showCenter">
            <CenterHeader class="centerHeader"></CenterHeader>
            <div class="form">
                <router-view></router-view>
            </div>
        </div>
    </div>
</template>

<script>
    import Aside from '../../components/center/Aside'
    import CenterHeader from '../../components/center/CenterHeader'

    export default {
        name: "center",
        data() {
            return {
                showCenter: true,
                centerPadding: '',
                screenWidth: document.body.clientWidth,
            }
        },
        mounted() {
            var that = this;
            window.onresize = function () {
                that.screenWidth = document.body.clientWidth;
            };
            if (that.screenWidth >= 1200) {
                that.centerPadding = 'padding-left: 200px;';
            } else if (that.screenWidth >= 768 && that.screenWidth < 1200) {
                that.centerPadding = 'padding-left: 64px;';
            } else {
                that.centerPadding = 'padding-left: 0px;';
            }
        },
        watch: {
            'screenWidth': function (newVal) {
                if (newVal >= 1200) {
                    this.centerPadding = 'padding-left: 200px;';
                } else if (newVal >= 768 && newVal < 1200) {
                    this.centerPadding = 'padding-left: 64px;';
                } else {
                    this.centerPadding = 'padding-left: 0px;';
                }
            }
        },
        methods: {
            changeCenterPadding() {
                this.showCenter = !this.showCenter;
            }
        },
        components: {
            Aside,
            CenterHeader
        }
    }
</script>

<style lang="stylus">
    .center-wrap {

        .center {
            padding-top 5px
            padding-right 0
            padding-bottom 30px

            .centerHeader {
                margin-top 60px
            }

            .form {
                margin 10px 20px 20px 20px
                padding 20px
                background-color #fff
                border-radius 5px
                border solid 1px #e6e6e6
            }
        }
    }
</style>
