import{$ as t,G as e,o as s}from"./chunk-94b083a2.js";t((async function(){e.createIframe({path:"cframe.html",id:"UNIQUE-ROOT-by69bq5xiupb",className:"UNIQUE-IFRAME-by69bq5xiupb",cssText:"\n    position: fixed;\n    top: 80px;\n    right: 40px;\n    z-index: 50;\n    min-width: 500px;\n    min-height: 250px;\n    border: none;\n    box-shadow: 0px 2px 11px 1px gray;\n    border-radius: 11px;\n    border: none;\n    z-index: 999;\n    "}),s("RESIZE",(async(t,e)=>{const{width:s,height:n}=t,c=document.getElementById("UNIQUE-ROOT-by69bq5xiupb");s&&c.style.width!==s&&(c.style.width=s),n&&c.style.height!==n&&(c.style.height=n),e({status:"success"})})),s("SHOW-OR-HIDE-IFRAME",(async(e,s)=>{const n=document.getElementById("UNIQUE-ROOT-by69bq5xiupb");n.style.display!==e.display?n.style.display=e.display:"block"===e.display&&t(n).fadeOut(198).fadeIn(198).fadeOut(198).fadeIn(198),s({status:"success"})})),s("POSITION",(async(t,e)=>{const s=document.getElementById("UNIQUE-ROOT-by69bq5xiupb");s.style.right=parseFloat(s.style.right)-t.offsetX+"px",s.style.top=parseFloat(s.style.top)+t.offsetY+"px",e({status:"success"})})),s("UPDATE-IFRAME-CSS",(async(t,e)=>{if(!t.cssObject)return;const s=document.getElementById("UNIQUE-ROOT-by69bq5xiupb"),n=Object.keys(t.cssObject);if("override"===t.mode){let e="";for(let s=n.length-1;s>=0;s--){const c=n[s];e+=`${c}:${t.cssObject[c]};`}s.setAttribute("style",e)}else for(let c=n.length-1;c>=0;c--){const e=n[c];s.style[e]=t.cssObject[e]}e({status:"success"})})),s("GET-IFRAME-CSS",(async(t,e)=>{const s=document.getElementById("UNIQUE-ROOT-by69bq5xiupb"),n={};for(let c=0;c<t.length;c++){const e=t[c];n[e]=s.style[e]}e(n)})),s("WINDOW-LOCATION",(async(t,e)=>{e(location)})),s("FOR-EXAMPLE",(async(t,e)=>{t.href&&(window.location.href=t.href),e({status:"success"})})),s("GET-CURRENT-HTML-STRING",(async(t,e)=>{if(!/^.+\.bing\.com\/maps\/?\?.*$/.test(window.location.href))return void e({code:502,error:"No Business Data."});e({code:200,htmlString:document.documentElement.outerHTML})})),s("DOWNLOAD-FILE",(async(t,s)=>{const{type:n,data:c}=t;n&&c?("csv"===n?e.downloadCSV(c,"Bing_Maps_Scraper_"+c.length+"_"):e.downloadXLSX(c,"Bing_Maps_Scraper_"+c.length+"_"),s({status:"success"})):s({status:"fail"})})),s("REQUEST-NEXT-PAGE-CHECK",(async(e,s)=>{let n=!1;const c=document.getElementsByClassName("bm_waitlayer");if(c.length>0){const e=c[c.length-1];if("block"!==window.getComputedStyle(e).getPropertyValue("display")){const e=t(".entity-listing-container").last().find("a.bm_rightChevron")[0]||null;if(e&&"none"!==e.style.display){n=!0;const t=new MouseEvent("click",{view:window,bubbles:!0,cancelable:!0});e.dispatchEvent(t)}}}s({hasNextPage:n})})),s("REQUEST-BVLIST-CHECK",(async(e,s)=>{const n=t(".b_vList");!n||n.length<=0||n.last().find("li a").length<0?s({code:500}):s({code:200})})),s("REQUEST-BVLIST-HTML-STRING",(async(e,s)=>{const n=t(".b_vList");!n||n.length<=0||n.last().find("li a").length<0?s({code:500,bvHtml:""}):s({code:200,bvHtml:n.last()[0].outerHTML})}))}));