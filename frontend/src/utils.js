/**
 * 下载文件
 * @param blob
 * @param fileName
 */
export function downloadFile (url, fileName) {
  const aLink = document.createElement('a')
  const evt = document.createEvent('HTMLEvents')
  evt.initEvent('click', true, true) // initEvent 不加后两个参数在FF下会报错  事件类型，是否冒泡，是否阻止浏览器的默认行为
  aLink.download = fileName
  aLink.href = url
  aLink.click()
}