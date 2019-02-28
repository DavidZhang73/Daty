<template>
    <div class="home-wrap">
        <div class="home">
            <el-row class="btn-row" :gutter="20">
                <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="1" :offset="9">
                    <router-link :to="{ name : 'about'}">
                        <el-button type="primary" icon="el-icon-download">我要收文件</el-button>
                    </router-link>
                </el-col>
                <el-col :xs="8" :sm="6" :md="4" :lg="3" :xl="1">
                    <el-button type="primary" icon="el-icon-upload2">我要交文件</el-button>
                </el-col>
            </el-row>
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

        .home {


            .btn-row {
                padding-top 430px
            }
        }
    }
</style>
