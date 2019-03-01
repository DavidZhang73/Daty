<template>
    <div class="home-wrap">
        <div class="home">
            <el-row class="btn-row">
                <el-col :offset="10" :span="4">
                    <el-button-group>
                        <router-link :to="{ name : 'fileDetail'}">
                            <el-button type="primary" icon="el-icon-download">我要收文件</el-button>
                        </router-link>
                        <router-link :to="{ name : 'about'}">
                            <el-button type="primary" icon="el-icon-upload2">我要交文件</el-button>
                        </router-link>
                    </el-button-group>
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

        background: #F8F9FB url("../assets/background.jpg") no-repeat;
        background-size: contain;

        .home {


            .btn-row {
                padding-top 430px
            }
        }
    }
</style>
