<template>
    <div class="fileUploadAndDownload-wrap">
        <el-row>
            <el-col :xs="{span:24}"
                    :sm="{span:24}"
                    :lg="{span:24}">
                <el-collapse v-model="activeNames">
                    <el-collapse-item v-for="item in items" :name="item.userGroupID">
                        <template slot="title">
                            {{item.userGroupTitle}}
                            <el-tag
                                    v-if="item.url"
                                    size="mini"
                                    type="success"
                                    effect="light">已提交
                            </el-tag>
                            <el-tag v-else
                                    size="mini"
                                    type="danger"
                                    effect="light">未提交
                            </el-tag>
                        </template>
                        <el-upload
                                :action="action"
                                :before-upload="beforeUploadCheck"
                                :on-error="uploadErr"
                                :on-remove="uploadRemove"
                                :on-success="uploadSuc"
                                :before-remove="beforeRemove"
                                :file-list="fileList"
                                :limit="1">
                            <el-button size="small" type="primary" plain>点击上传</el-button>
                            <div slot="tip" class="el-upload__tip">文件大小不得超过10MB,每个文件集只能存在一个模板文件,请删除原文件后再上传</div>
                        </el-upload>
                        <el-button
                                class="downloadBtn"
                                size="small"
                                type="info"
                                plain>下载文件</el-button>
                    </el-collapse-item>
                </el-collapse>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "fileUploadAndDownload",
        data() {
            return {
                action: 'https://jsonplaceholder.typicode.com/posts/',
                activeNames: [],
                fileList: [],
                items: [
                    {
                        userGroupTitle: 'test-1',
                        userGroupID: 1,
                        url: ''
                    },
                    {
                        userGroupTitle: 'test-2',
                        userGroupID: 2,
                        url: '123'
                    },
                    {
                        userGroupTitle: 'test-3',
                        userGroupID: 3,
                        url: '123'
                    }
                ]
            }
        },
        methods: {
            beforeUploadCheck(file) {
                let isLt10M = file.size / 1024 / 1024 < 10;
                if (!isLt10M) {
                    this.$message.error('上传失败，文件大小超过10MB !');
                }
                return isLt10M;
            },
            uploadErr() {
                this.$message.error('上传失败，请尝试重新上传 !');
            },
            uploadRemove() {
                this.fileList.pop();
                //TODO
            },
            uploadSuc(response, file) {
               //TODO
                let fileObj = {};
                fileObj.name = file.name;
                fileObj.uid = file.uid;
                this.fileList.push(fileObj);
                console.log(this.fileList);
            },
            beforeRemove(file) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
        }
    }
</script>

<style lang="stylus">
    .fileUploadAndDownload-wrap {
        width 100%

        .el-collapse {
            width 100%

            .el-collapse-item {
                width 100%

                .el-tag {
                    margin-left 10px
                }

                .el-upload {
                    margin 10 10 0 10
                }

                .downloadBtn {
                    margin 10 10 10 10
                }
            }
        }
    }
</style>