<template>
    <div class="home-wrap">
        <div class="home">
            <el-row class="btn-row">
                <el-col :offset="10" :span="4">
                    <el-button-group>
                        <router-link
                                :to="{ name : 'fileDetail'}"
                                class="el-button el-button--primary">
                            <i class="el-icon-download"></i>
                            我要收文件
                        </router-link>
                        <router-link :to="{ name : 'about'}"
                                     class="el-button el-button--primary">
                            <i class="el-icon-upload2"></i>
                            我要交文件
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
                padding-top 500px
            }
        }
    }
</style>
