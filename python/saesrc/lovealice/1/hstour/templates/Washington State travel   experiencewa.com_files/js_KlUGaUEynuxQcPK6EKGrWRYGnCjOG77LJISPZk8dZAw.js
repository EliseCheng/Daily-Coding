
//create hookJS object
var hookJS = {};
hookJS.help = {};
hookJS.help.basic = 'The function saved in hookJS.hook.hook_name will run when the hook is called.';
hookJS.help.register_a_hook_function = 'To add your function to a given hook, simply save a function into this object  example: hookJS.hook.gridDataWrite.someKey = someVariableAsFunction  It will run whenever the hook gridDataWrite is called by the core code. Instead of a variable as function, you can also run line(s) of code.  Example: hookJS.hook.dataWrite.someKey = \'alert("I ran");\'';
hookJS.help.create_a_hook = 'To create a hook, add a new hook object to hookJS.hook.   Example: hookJS.hook.myNewHookName = {};  This is the container to store the functions you want to run when the hook is fired.';
hookJS.help.fire_a_hook = 'In your code when you want the hook to run, simply call hookJS.runHook(\'myNewHookName\');  Calling this function will run the hook function and return the number that were run (useful for debugging).';
hookJS.hook = {};
hookJS.runHook = function(sHookName) {
    iCount = 0;
    if ((typeof hookJS.hook[sHookName] === 'object') && (Object.keys(hookJS.hook[sHookName]).length > 0)) {
        iCount = hookJS.hook[sHookName].length;
        for (var key in  hookJS.hook[sHookName]) {
            if (typeof hookJS.hook[sHookName][key] === 'string') {
                eval(hookJS.hook[sHookName][key]);
            } else if (typeof hookJS.hook[sHookName][key] === 'function') {
                hookJS.hook[sHookName][key]();
            }
        }
        return iCount;
    }
    ;
};
//end hookJS
;
