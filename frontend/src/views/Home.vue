<template>
	<div class="home-wrap">
		<Background img-name="background.jpg"
		            :blur="false"></Background>
		<div class="home">
			<img class="logo" src="../assets/home_logo.svg" alt="LOGO">
			<div class="button-row">
				<router-link :to="{name: 'home'}">
					<el-button type="primary">
						<i class="el-icon-download"></i>
						我要收文件
					</el-button>
				</router-link>
				<router-link :to="{name: 'home'}">
					<el-button type="primary" id="last-btn">
						<i class="el-icon-upload2"></i>
						我要交文件
					</el-button>
				</router-link>
			</div>
		</div>
	</div>
</template>

<script>
    import Background from '../components/Background'

    export default {
        name: 'home',
        components: {
            Background
        }
    }
</script>

<style lang="stylus">
	.home-wrap {
		height 100%
		background-size: contain;
		background-color rgb(248, 250, 251)

		.home {
			position relative
			padding-top 200px
			margin 0 auto
			width 500px

			.logo {
				width 512px
				height 256px
				margin-bottom 80px
			}

			.button-row {
				margin 0 auto
				width 350px

				button {
					font-size 16px
				}

				#last-btn {
					float right

					&::after {
						content ''
						display block
						clear both
					}
				}
			}
		}
	}
</style>
