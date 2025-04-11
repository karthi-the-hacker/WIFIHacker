(function(b){b.fn.FrontierAjaxForm=function(a,k){a=a||{};var l=this.attr("tagName");if(!l||"form"===l.toLowerCase()){var c=this,h={type:"POST",success:function(d){b.fn.hideFormLoader(c.attr("id"));a.successCallback&&(a.responseText=d.responseText,a.successCallback.call(this,a))},error:function(){a.validator&&a.validator.messages&&a.validator.messages.globalSubmitError&&window.alert(a.validator.messages.globalSubmitError);b.fn.hideFormLoader(c.attr("id"))},formError:function(d){if(d.fieldErrors){var r=
d.fieldErrors;if(f){var e={};b.each(r,function(a,c){b("#"+a).attr("name")&&(e[b("#"+a).attr("name")]=c)});a.extendedSettings&&"function"===typeof a.extendedSettings.markCustomErrors&&a.extendedSettings.markCustomErrors(d,e);f.showErrors(e);"function"===typeof f.settings.invalidHandler&&(f.invalid=e,f.settings.invalidHandler(c,f))}}!a.extendedSettings&&d.globalError&&window.alert(d.globalError);b.fn.hideFormLoader(c.attr("id"))},useJQM:!1,callbackSmartLock:a.callbackSmartLock||null};a.validator&&b.extend(a.validator,
{submitHandler:function(){h.data=c.serialize();b.fn.showFormLoader(c.attr("id"));b.fn.FrontierAjaxRequest(c.attr("action"),h,c)}});var f=a.validator&&"object"===typeof a.validator&&"function"===typeof this.validate?this.validate(a.validator):null;f||this.bind("submit",function(){b.fn.showFormLoader(c.attr("id"));b.fn.FrontierAjaxRequest(c.attr("action"),h,c)});this.showErrors=h.formError;return this}};b.fn.FrontierAjaxRequest=function(a,k,l){var c=k.success,h=k.error,f=/throw \/\*LI:DBE\*\/ 1;/;k.success=
void 0;k.error=void 0;var d=b.extend({},{type:"GET",dataType:"text",statusCode:{500:function(a,b,c){h.call(this,a,b,c)}},error:function(a,b,c){h.call(this,a,b,c)},success:function(a,e,h){var g=a.replace(f,"")||"{}",g=b.parseJSON(g),m=g.redirectUrl||"",p=g.errors||null,n=g.content||"";e="ok";var q=b(l);if(g.submitRequired&&l)return l[0].submit(),!1;!1===g.success&&(e="fail");g.status&&(e=g.status.toLowerCase());if("ok"===e){if(m&&!n){navigator.credentials&&"function"===typeof k.callbackSmartLock&&
q.length&&"true"===q.attr("data-existingmembersignin")?k.callbackSmartLock(m):window.location.href=m;return}if(n){a={};a.responseText=n;c(a);return}window.location.reload()}"fail"===e?p&&"post"===d.type.toLowerCase()&&d.formError&&d.formError.call(this,p):c.call(this,a,e,h)},headers:{"X-IsAJAXForm":"1"}},k);b.ajax(a,d)}})(jQuery);$.LI={};$.LI.i18n={register:function(a,b){$.LI.i18n[a]||($.LI.i18n[a]=b)},get:function(a,b){return $.LI.i18n[a]||""}};(function(w){$("#login").on("pageinit",function(){function b(){function a(a){a.siblings("label").first()[0<a.val().length?"addClass":"removeClass"]("show")}g.on("input blur",_.throttle(function(){a(g)},250));q.on("input blur",_.throttle(function(){a(q)},250))}var h=$(this).find("form#loginForm"),d=!!document.getElementById("pagekey-uas-consumer-login-internal"),e=$("form#one-time-password-form input[name\x3dsession_key]"),n=h.hasClass("phone-reg-enabled"),k=h.hasClass("phone-reg-enabled-fullsupport"),
c;try{c=window.self!==window.top}catch(u){c=!0}c=!c&&navigator.credentials&&"true"===h.attr("data-existingmembersignin");var r=$("#forgot-password"),g=$("#session_key-login"),q=$("#session_password-login"),v=h.find("input[name\x3dsource_app]").val(),s=r.attr("href"),l=$("#domainSuggestion"),p,m,k={focusInvalid:!0,rules:{session_key:{required:!0,email:{depends:function(a){return!(RegExp(/^[0-9- ()+]*$/gm).test(a.value)&&n)}}}},messages:{session_key:{required:$.LI.i18n.get(k?"consumer_login_mobile__form_error__enter_email_or_phone":
"consumer_login_mobile__form_error__enter_email"),email:$.LI.i18n.get(k?"consumer_login_mobile__form_error__enter_valid_email_or_phone":"consumer_login_mobile__form_error__enter_valid_email")},session_password:{required:$.LI.i18n.get("consumer_login_mobile__form_error__enter_password")}}},t=h.FrontierAjaxForm({validator:k,extendedSettings:{markCustomErrors:function(a,f){"wp"===a.ec?(f[$("#session_password-login").attr("name")]=a.globalError,d&&e.length&&e.val(g.val())):"iu"===a.ec||"ium"===a.ec?(f[$("#session_key-login").attr("name")]=
a.globalError,""!==a.domainSuggestions&&($("#suggestion").text(a.domainSuggestions),l.hasClass("hide")&&l.removeClass("hide"))):!a.ec&&a.globalError&&LI.showMobileError({message:a.globalError});""===a.domainSuggestions&&(l.hasClass("hide")||l.addClass("hide"));$("#tryCount").val(a.tc)}},callbackSmartLock:c&&"function"===typeof LI.smartLockSaveCredentials?LI.smartLockSaveCredentials:null});(function(){r.click(function(a){var f=g.val();a.target.href=LI.patterns.email.test(f)?LI.addParams(s,{email:encodeURIComponent(f)}):
s})})();(function(){function a(a){var b=g.val();a.target.href=LI.patterns.email.test(b)?LI.addParams(m,{email:encodeURIComponent(b)}):m}"regLoginFailure"===LI.parseQueryString(window.location.href).ec&&(p=JSON.parse('{"fieldErrors": {}, "tc": 1, "ec": "wp"}'),m=$("#forgotRegPasswordURL").val(),p.globalError=$.LI.i18n.get("consumer_login_mobile__text_plain__wrong_password_from_reg")+' \x3ca id\x3d"forgetRegPasswordLink" href\x3d"'+m+'"\x3e'+$.LI.i18n.get("consumer_login_mobile__text_plain__password_reminder")+
"\x3c/a\x3e",t.showErrors(p),$("#forgetRegPasswordLink").on("click",a))})();"cap"===v&&b();c&&"function"===typeof LI.smartLockGetCredentials&&LI.smartLockGetCredentials(t.showErrors)});var d=$("#session_key-login"),u=$("#mini-profile"),e=$("#not-me--js"),n=$("#suggestion");e.show();e.on("click",function(b){d.show();u.hide();e.hide();d.focus()});n.on("click",function(){var b=n.text(),b=d.val().split("@")[0].concat(b);d.val(b);$("#clickedSuggestion").val("true")})})($(document));(function(a){var b=a("#login"),c=a("#one-time-password-form");b.on("click",".one-time-password-url",function(a){a.preventDefault();a.stopPropagation();c.submit()})})(jQuery);