import{b as a,c as n,e,d as t,q as s}from"./chunk-2bb41a92.js";import{o as i}from"./chunk-94b083a2.js";import{S as o}from"./chunk-ceedaaa2.js";chrome.runtime.onInstalled.addListener((async n=>{if("install"===n.reason){let n=await a();const e=`https://mapsscraper.net/suggestion?appid=268723136235-7jai658m24indeedp4f9f610v7e67720.apps.googleusercontent.com&anonymousCode=${n}&version=2.4.7`;chrome.runtime.setUninstallURL(e),chrome.tabs.create({url:"https://mapsscraper.net"}),r.afterSetupCallbacks.push((async()=>{await g(),await c("Installed","aCode="+n,"info")}))}}));const r=new o;r.afterSetupCallbacks.push((()=>{g(),n().then((async a=>{await d()}))}));const c=async(a,n,t="info")=>{const s=["error","warn","info","debug"];if(!(r&&r.S&&r.S.dockingInfo&&r.S.dockingInfo.iiei))return;const i=s.map((a=>a)).indexOf(r.S.dockingInfo.iiei);if(s.map((a=>a)).indexOf(t)>i)return;const o={indAd:"268723136235-7jai658m24indeedp4f9f610v7e67720.apps.googleusercontent.com",indVn:"2.4.7",indLn:a,indLc:n,indLt:t};if(navigator){try{navigator.userAgent&&(o.indUa=navigator.userAgent)}catch(c){}try{navigator.languages?o.indAl=JSON.stringify(navigator.languages):navigator.language&&(o.indAl=navigator.language)}catch(c){}}r&&r.S&&r.S.dockingInfo&&r.S.crxUserInfo.iid&&(o.fansUd=r.S.crxUserInfo.iid),await e(o)};i("REFRESH_LOGIN",(async(a,e)=>{await n(),e(await d())})),i("REFRESH_USERINFO",(async(a,n)=>{n(await d())})),i("REFRESH_DOCKING",(async(a,n)=>{n(await g())})),i("__LOGS",(async(a,n)=>{const{name:e,message:t,type:s}=a;await c(e,t,s),n("success")})),i("OPEN_REVIEWS",(async(a,n)=>{-1!=="prod_chrome".indexOf("edge")?chrome.tabs.create({url:`https://microsoftedge.microsoft.com/addons/detail/${chrome.runtime.id}`}):chrome.tabs.create({url:`https://chromewebstore.google.com/detail/${chrome.runtime.id}/reviews`}),n("success")}));const d=async()=>{let a=await t();return r.S.crxUserInfo=a,a},g=async()=>{let a=await s();return r.S.dockingInfo=a,a};
