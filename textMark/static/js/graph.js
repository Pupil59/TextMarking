option = {
    title: {
        text: '',
        x: 'center'
    },
    //—— 悬浮框 ——
    tooltip: {
        trigger: 'item',
        formatter: function(x) {
            return x.data.label; //设置提示框的内容和格式 节点和边都显示name属性
        },
    },
    legend: [{
        orient: 'vertical',
        x: 'left',
        y: '50px',
        itemWidth: 14,
        itemHeight: 14,
        data: [ //节点数据

            {
                name: 'stu7',
                icon: 'circle'
            },
            {
                name: 'stu8',
                icon: 'circle'
            }, {
                name: 'stu9',
                icon: 'circle'
            }, {
                name: 'stu10',
                icon: 'circle',

            }, {
                name: 'stu11',
                icon: 'circle'
            },

        ],
    }, ],
    toolbox: {
        show: true, //是否显示工具箱
        feature: {
            saveAsImage: true // 保存为图片，
        }
    },
    //—— 其他设置 ——
    animationDurationUpdate: 1500,
    animationEasingUpdate: 'quinticInOut',
    series: [{
        type: 'graph',
        layout: 'circular', // 'circular' ,force
        symbolSize: 30, //图形的大小（示例中的圆的大小）
        roam: true, //鼠标缩放及平移
        focusNodeAdjacency: true, //是否在鼠标移到节点上的时候突出显示节点、节点的边和邻接节点
        label: {
            normal: {
                show: true, //控制非高亮时节点名称是否显示
                position: '',
                fontSize: 18,
                color: 'black'
            },
            emphasis: {
                show: true, //控制非高亮时节点名称是否显示
                position: 'right',
                fontSize: 16,
                color: 'black'
            },
        },
        force: {
            x: 'center',
            y: '50px',
            edgeLength: 180,
            //repulsion: 8000
        },
        //     edgeSymbol: ['circle', 'arrow'],//箭头
        //    edgeSymbolSize: [6, 10],
        edgeLabel: {
            normal: {
                show: false,
                textStyle: {
                    fontSize: 12
                },
                formatter: "{c}"
            },
            emphasis: {
                show: true,
                textStyle: {
                    fontSize: 14 //边节点显示的字体大小
                }
            },
        },


        


        categories: [ //节点数据            
            {
                name: 'stu7',
                icon: 'circle'
            },
            {
                name: 'stu9',
                icon: 'circle'
            },

        ],



    }]
}; // 使用刚指定的配置项和数据显示图表。