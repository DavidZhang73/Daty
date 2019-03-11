<template>
	<div class="test-wrap">
		<p>{{msg}}</p>
		<button @click="handle">Test</button>
	</div>
</template>

<script>
    import api from '../api'

    export default {
        name: "Test",
        data() {
            return {
                msg: ''
            }
        },
        methods: {
            handle() {
                api.test().then(data => {
                    this.msg = data
                })
            }
        }
    }
</script>

<style lang="stylus">
	.test-wrap {
		margin 120px 0 0 200px
		height 100px
		width 100px
	}
</style>
