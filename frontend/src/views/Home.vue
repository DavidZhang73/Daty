<template>
    <div class="home-wrap">
        <div class="home">
            <div class="button-col">
                <div class="button-row">
                    <router-link
                            :to="{ name : 'fileDetail'}">
                        <el-button type="primary" class="button1">
                            <i class="el-icon-download"></i>
                            我要收文件
                        </el-button>
                    </router-link>
                    <router-link :to="{ name : 'about'}">
                        <el-button type="primary" class="button2">
                            <i class="el-icon-upload2"></i>
                            我要交文件
                        </el-button>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'home',
        components: {}
    }
</script>

<style lang="stylus">
    .home-wrap {
        height 100%

        background: #F8F9FB url("../assets/background.jpg") no-repeat;
        background-size: contain;

        .home {
            height inherit

            .button-col {
                height inherit
                width 270px
                margin 0 auto
                /*border 1px solid black*/

                .button-row {
                    position relative
                    top 55%
                    /*border 1px solid blue*/

                    .button1 {
                        float left
                    }

                    .button2 {
                        float right
                    }

                }
            }
        }
    }
</style>
