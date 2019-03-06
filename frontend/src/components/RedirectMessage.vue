<template>
	<div class="redirect-wrap" v-cloak>
		<p>{{this.message}}</p>
		<p>{{this.countdown}} 秒后自动跳转到{{this.jump_to_name}}。</p>
		<p>
			<router-link :to="{path: this.jump_to_path}">我知道了，点我直接跳转</router-link>
		</p>
	</div>
</template>

<script>
    export default {
        name: "RedirctMessage",
        data() {
            return {
                countdown: 5,
            }
        },
        props: {
            message: String,
            jump_to_path: String,
            jump_to_name: String,
        },
        mounted() {
            let timer = setInterval(() => {
                if (this.countdown === 0) {
                    clearInterval(timer);
                    this.$router.push({path: this.jump_to_path})
                }
                this.countdown--
            }, 1000);
        }
    }
</script>

<style lang="stylus">
	.redirect-wrap {
		text-align center

		p {
			font-size 18px

			a {
				opacity 0.8

				&:hover {
					opacity 1
				}
			}
		}
	}
</style>
