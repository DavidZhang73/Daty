<template>
    <div class="centerHeader-wrap">
        <p>{{title}}</p>
    </div>
</template>

<script>
    export default {
        name: "CenterHeader",
        data() {
            return {
                title: '',
            }
        },
        mounted() {
            if (this.$route.name === 'collectionList') {
                this.title = '文件集列表';
            } else if (this.$route.name === 'groupList') {
                this.title = '用户组列表';
            } else if (this.$route.name === 'addNewGroup') {
                this.title = '新增用户组';
            } else if (this.$route.name === 'userInfo') {
                this.title = '修改个人信息';
            } else if (this.$route.name === 'editUserGroup') {
                this.title = '编辑用户组'
            } else {
                this.title = '修改密码';
            }
        },
        watch: {
            $route: function (newVal) {
                if (newVal.name === 'groupList') {
                    this.title = '用户组列表';
                } else if (newVal.name === 'addNewGroup') {
                    this.title = '新增用户组';
                } else if (newVal.name === 'userInfo') {
                    this.title = '修改个人信息';
                } else if (newVal.name === 'userPassword') {
                    this.title = '修改密码';
                } else if (newVal.name === 'editUserGroup') {
                    this.title = '编辑用户组'
                } else {
                    this.title = '文件集列表';
                }
            }
        }
    }
</script>

<style lang="stylus">
    .centerHeader-wrap {
        background-color white

        p {
            padding 17px 0px 17px 40px
            border-bottom 1px solid #e6e6e6
        }
    }
</style>