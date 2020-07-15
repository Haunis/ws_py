"""
获取标签资源：使用chrome浏览器，按f12,点击左侧箭头按钮“select an element in the page to inspect it”即可
demo演示：过滤调标签，保存内容描述
"""
import re

origin_str = """
<dl class="job_detail" id="job_detail">
    <dt class="clearfix join_tc_icon">
    </dt>
    <dd class="job-advantage">
        <span class="advantage">职位诱惑：</span>
        <p>补充公积金 年终奖 免费咖啡</p>
    </dd>
    <dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>Android开发工程师</p>
<p><br></p>
<p>岗位职责：</p>
<p>1、使用Java/C编写定位算法交付SDK</p>
<p>2、负责SDK相关技术调研、优化、基础库和组件搭建</p>
<p>3、对技术有强烈的进取心，具有良好的沟通能力和团队合作精神、优秀的分析和解决复杂问题的能力</p>
<p><br></p>
<p>岗位要求：</p>
<p>1、本科或以上学历，计算机相关专业，三年以上移动端开发经验；</p>
<p>2、熟练使用C、Java等开发语言，熟悉常用数据结构和算法；</p>
<p>3、熟悉Android 平台及框架原理，熟悉Android的基本组件使用；</p>
<p>4、熟悉NDK/JNI开发，熟悉Android平台SDK开发；</p>
<p>5、有Android性能、安全方面的经验者优先；有定位行业经验优先；</p>
        </div>
    </dd>
    <!-- Leader专访 -->
            <!-- Leader专访 end -->
    <!-- 团队Leader -->
        <!-- 团队Leader end -->
    <dd class="job-address clearfix">
                <h3 class="address">工作地址</h3>
        <div class="work_addr">
                                                <a rel="nofollow" href="https://www.lagou.com/jobs/list_?city=上海#filterBox">上海</a> -
                    <a rel="nofollow" href="https://www.lagou.com/jobs/list_?city=上海&amp;district=杨浦区#filterBox">杨浦区</a>
                                            - 国权北路1688弄湾谷科技园C5栋9楼
                                                            <a rel="nofollow" href="javascript:;" id="mapPreview">查看地图</a>
        </div>
        <div id="miniMap" class="amap-container" style="position: relative; background: rgb(252, 249, 242);"><object style="display: block; position: absolute; top: 0; left: 0; height: 100%; width: 100%; overflow: hidden; pointer-events: none; z-index: -1;" type="text/html" data="about:blank"></object><div class="amap-maps"><div class="amap-drags" style=""><div class="amap-layers" style="transform: translateZ(0px);"><div class="amap-layer" style="position: absolute; z-index: 0; top: 0px; left: 0px;"><img src="https://wprd03.is.autonavi.com/appmaptile?lang=zh_cn&amp;size=1&amp;style=7&amp;x=3430&amp;y=1672&amp;z=12&amp;scl=1&amp;ltype=3" style="position: absolute; top: -49px; left: -108px; width: 256px; height: 256px; z-index: 12;"></div><div class="amap-markers" style="position: absolute; z-index: 120; top: 0px; left: 0px;"><div class="amap-marker" style="top: -31px; left: -9px; z-index: 100; transform: rotate(0deg); transform-origin: 9px 31px; display: block;"><div class="amap-icon" style="position: absolute; width: 19px; height: 33px; opacity: 1;"><img src="https://webapi.amap.com/theme/v1.3/markers/n/mark_bs.png" style="width: 19px; height: 33px; top: 0px; left: 0px;"></div></div></div><canvas class="amap-labels" draggable="false" width="0" height="0" style="position: absolute; z-index: 99; height: 0px; width: 0px; top: 0px; left: 0px;"></canvas></div><div class="amap-overlays" style=""></div></div></div><div style="display: none;"></div><div class="amap-controls"></div><a class="amap-logo" href="http://gaode.com" target="_blank"><img src="https://webapi.amap.com/theme/v1.3/logo@1x.png?v=2"></a><div class="amap-copyright" style="display: none;"><!--v1.3.28--> © 2020 AutoNavi <span class="amap-mcode">- GS(2018)1709号</span></div></div>
                <input type="hidden" name="positionLng" value="121.501915">
        <input type="hidden" name="positionLat" value="31.339391">
        <input type="hidden" name="positionAddress" value="国权北路1688弄湾谷科技园C5栋9楼">
        <input type="hidden" name="workAddress" value="上海">
        <div style="display: none;">
            <div id="mapPopup" class="popup">
                <div id="fullMap" class="amap-container" style="position: relative; background: rgb(252, 249, 242);"><object style="display: block; position: absolute; top: 0; left: 0; height: 100%; width: 100%; overflow: hidden; pointer-events: none; z-index: -1;" type="text/html" data="about:blank"></object><div class="amap-maps"><div class="amap-drags" style=""><div class="amap-layers" style="transform: translateZ(0px);"><div class="amap-layer" style="position: absolute; z-index: 0; top: 0px; left: 0px;"><img src="https://wprd01.is.autonavi.com/appmaptile?lang=zh_cn&amp;size=1&amp;style=7&amp;x=27443&amp;y=13377&amp;z=15&amp;scl=1&amp;ltype=3" style="position: absolute; top: -133px; left: -96px; width: 256px; height: 256px; z-index: 15;"></div><div class="amap-markers" style="position: absolute; z-index: 120; top: 0px; left: 0px;"><div class="amap-marker" style="top: -31px; left: -9px; z-index: 100; transform: rotate(0deg); transform-origin: 9px 31px; display: block;"><div class="amap-icon" style="position: absolute; width: 19px; height: 33px; opacity: 1;"><img src="https://webapi.amap.com/theme/v1.3/markers/n/mark_bs.png" style="width: 19px; height: 33px; top: 0px; left: 0px;"></div></div></div><canvas class="amap-labels" draggable="false" width="0" height="0" style="position: absolute; z-index: 99; height: 0px; width: 0px; top: 0px; left: 0px;"></canvas></div><div class="amap-overlays" style=""></div></div></div><div style="display: none;"></div><div class="amap-controls"><div class="amap-toolbar" style="left: 10px; top: 10px; visibility: visible;"><div class="amap-pancontrol" style="position: relative; display: block;"><div class="amap-pan-left"></div><div class="amap-pan-top"></div><div class="amap-pan-right"></div><div class="amap-pan-bottom"></div></div><div class="amap-locate" style="position: relative; left: 17px; display: block;"></div><div class="amap-zoomcontrol" style="position: relative; left: 14px;"><div class="amap-zoom-plus"></div><div class="amap-zoom-ruler" style="display: block;"><div class="amap-zoom-mask" style="height: 27px;"></div><div class="amap-zoom-cursor" style="top: 27px;"></div><div class="amap-zoom-labels"><div class="amap-zoom-label-street"></div><div class="amap-zoom-label-city"></div><div class="amap-zoom-label-province"></div><div class="amap-zoom-label-country"></div></div></div><div class="amap-zoom-minus"></div></div></div><div class="amap-overviewcontrol" style="width: 17px; height: 17px; visibility: visible;"><div class="amap-overview-main" style="width: 115px; height: 115px;"><div class="amap-overview-map" style="width: 115px; height: 115px;"><img src="https://webrd01.is.autonavi.com/appmaptile?lang=zh_cn&amp;size=1&amp;scale=1&amp;style=7&amp;x=6&amp;y=3&amp;z=3" style="visibility: inherit; position: absolute; left: -121.711px; top: -10.5949px;"></div><div class="amap-overview-win" style="display: none;"></div><div class="amap-overview-win" style="display: none;"></div></div><div class="amap-overview-button" style="background-position: -40px -405px;"></div></div><div class="amap-scalecontrol" style="left: 2px; bottom: 20px; visibility: visible;"><div class="amap-scale-text" style="width: 57.0159px;">200 米</div><div class="amap-scale-line"><div class="amap-scale-edgeleft"></div><div class="amap-scale-edgeright" style="left: 50.0159px;"></div><div class="amap-scale-middle" style="width: 49.0159px;"></div></div></div></div><a class="amap-logo" href="http://gaode.com" target="_blank"><img src="https://webapi.amap.com/theme/v1.3/logo@1x.png?v=2"></a><div class="amap-copyright" style="display: none;"><!--v1.3.28--> © 2020 AutoNavi <span class="amap-mcode">- GS(2018)1709号</span></div></div>
            </div>
        </div>
    </dd>
    <!-- 职位发布者 -->
    <dd class="jd_publisher">
        <h3>职位发布者:</h3>
        <div class="border clearfix">
                        <img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/5D/63/CgpEMlmK2oOAPW4RAAAYRM_zW64061.jpg" width="60" height="60">
                        <div class="publisher_name">
                <a title="招聘小秘">
                                        <span class="name">招聘小秘</span>
                                                                <span class="chat_me" data-is-brief-style="1" data-lg-tj-id="1WG0" data-lg-tj-no="idnull" data-lg-tj-cid="idnull" data-lg-tj-track-code="jobs_code" data-lg-tj-track-type="1"></span>
                                        <input type="hidden" class="hr_portrait" value="i/image/M00/5D/63/CgpEMlmK2oOAPW4RAAAYRM_zW64061.jpg">
                    <input type="hidden" class="hr_name" value="招聘小秘">
                    <input type="hidden" class="hr_position" value="首席招聘官">
                    <input type="hidden" class="target_hr" value="8658127">
                    <input type="hidden" class="target_position" value="7096987">
                </a>
                <span class="pos"> 首席招聘官 </span>
                <span class="circle"></span>
                <span class="time" id="timeInfo">当前在线</span>
                            </div>
                                                </div>
    </dd>
    <!-- 职位发布者 end -->
</dl>
"""
# print(origin_str)

# origin_str = """
# <dl class="job_detail" id="job_detail">
#     <dt class="clearfix join_tc_icon">
#     </dt>
#     <dd class="job-advantage">
#         <span class="advantage">职位诱惑：</span>
#         <p>补充公积金 年终奖 免费咖啡</p>
#     </dd>
# """
ret = re.sub(r"<\w*>|<\w*\s.*\">|</\w*>|</\w*\s.*\">","",origin_str) #用空格替代标签
print(ret)

# ret =  re.findall(r"<\w*>|<\w* .*\">|</\w*>|</\w* .*\">",origin_str)
# for temp in ret:
#     print(temp)