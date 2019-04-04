<template>
    <el-row class="editUserGroup-wrap"
            v-loading="Loading"
            element-loading-text="拼命加载中"
            element-loading-spinner="el-icon-loading"
            element-loading-background="rgba(0, 0, 0, 0.8)">
        <el-col :xs="{span:24}"
                :sm="{span:20}"
                :lg="{span:18}">
            <el-form class="userGroupForm"
                     :model="userGroupForm"
                     ref="userGroupForm"
                     :rules="userGroupFormRules"
                     label-position="left"
                     label-width="100px"
                     status-icon>
                <el-form-item prop="type" label="用户组类型">
                    <el-radio-group v-model="userGroupForm.type" disabled>
                        <el-radio v-for="item in radioOptions"
                                  :label="item.value">{{item.label}}
                        </el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="用户组名称" prop="name">
                    <el-input v-model.trim="userGroupForm.name" placeholder="请输入用户组名称"></el-input>
                </el-form-item>
            </el-form>
        </el-col>
    </el-row>
</template>

<script>
    import api from '../../api'

    export default {
        name: "EditUserGroup",
        data() {
            return {
                Loading: true,
                userGroupForm: {},
                userGroupFormRules: {},
                radioOptions: [],
            }
        },
        mounted() {
            this.Loading = true;
            api.getUserGroupById(this.$route.params, this.$route.params.id).then(data => {
                this.userGroupForm = data;
                console.log(this.userGroupForm);
                this.Loading = false;
            });
            api.getUserGroupType().then(data => {
                this.radioOptions = data;
            })
        },
        filters: {
            formatterType(value) {
                if (value === 'NONEEDLOGIN') return '不需要登陆';
                else if (value === 'ALREADYSIGNIN') return '需要登陆已注册';
                else return '需要登陆未注册';
            }
        }
    }
</script>

<style lang="stylus">

</style>