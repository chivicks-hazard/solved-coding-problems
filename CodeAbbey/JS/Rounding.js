const a = [-173200534, 0, 1502094988, -1856123750, 471123265, -1905733616, 506938880, 36172825, -1983448247, -1105732421, 0, -1497600540, -2063588672, 821605809];
const b = [37372, 94509, -169336, 671900, 37330, 69224, 35840, 97751, -80738, 60322, -34172, 117528, 73105, 49362];

const c = [];

for (let i = 0; i < 14; i++) {
    let d = a[i] / b[i];
    let e = d < 0 ? true : false;
    let f = e ? Math.ceil(d) : Math.floor(d);
    let g = e ? -1 : 1;
    let h = Math.abs(d - f);
    let j = f + (Math.round(h) * g);

    c.push(j);
    console.log(j);
};