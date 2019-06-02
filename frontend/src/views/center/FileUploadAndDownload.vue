<template>
    <div class="fileUploadAndDownload-wrap">
        <el-row v-loading="Loading"
                element-loading-text="拼命加载中"
                element-loading-spinner="el-icon-loading"
                element-loading-background="rgba(255, 255, 255, 1)">
            <el-col :xs="{span:24}"
                    :sm="{span:24}"
                    :lg="{span:24}">
                <div class="title" align="center">
                    <h1 class="text">{{collectionInfo.name}}</h1>
                    <h6>创建人：{{creator.username}}</h6>
                </div>
                <el-divider content-position="left">起止时间</el-divider>
                <p class="time">提交开始时间：{{collectionInfo.start_datetime}}</p>
                <p class="time">提交截至时间：{{collectionInfo.end_datetime}}</p>
                <el-divider content-position="left">文件要求</el-divider>
                <p class="require">{{collectionInfo.description}}</p>
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
                            <el-popover
                                    placement="top-start"
                                    title="注意！"
                                    width="200"
                                    trigger="hover"
                                    content="文件大小不得超过10MB,每个文件集只能存在一个模板文件,请删除原文件后再上传">
                                <el-button
                                        size="small"
                                        type="primary"
                                        plain
                                        slot="reference">点击上传
                                </el-button>
                            </el-popover>
                        </el-upload>
                        <el-button
                                class="downloadBtn"
                                size="small"
                                type="info"
                                @click="downloadFile"
                                plain>下载文件
                        </el-button>
                    </el-collapse-item>
                </el-collapse>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import api from '../../api'

    export default {
        name: "fileUploadAndDownload",
        data() {
            return {
                Loading: true,
                action: 'https://jsonplaceholder.typicode.com/posts/',
                collectionInfo: {},
                creator: {},
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
        mounted() {
            this.getCollectionInfo();
        },
        methods: {
            getCollectionInfo() {
                this.Loading = true;
                api.getCollectionById(this.$route.params.id).then(data => {
                    this.collectionInfo = data;
                    this.creator = data.creator;
                    this.Loading = false;
                });
            },
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
            downloadFile() {
                //TODO
            }
        }
    }
</script>

<style lang="stylus">
    .fileUploadAndDownload-wrap {
        width 100%

        .title {

            .text {
                margin 10px 0 10px 0
            }
        }

        .time {
            margin 5px 20px 0 20px
        }

        .require {
            margin 5px 20px 20px 20px
        }

        .el-collapse {
            width 100%

            .el-collapse-item {
                width 100%

                .el-tag {
                    margin-left 10px
                }

                .el-upload {
                    margin 10px 10px 0 10px
                }

                .downloadBtn {
                    margin 10px 10px 0 10px
                }
            }
        }
    }
</style>