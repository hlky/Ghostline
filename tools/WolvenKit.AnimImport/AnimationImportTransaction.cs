internal static class AnimationImportTransaction
{
    public static async Task<bool> RunAsync(
        string destination,
        Func<DirectoryInfo, string, Task<bool>> importAndValidate
    )
    {
        var parent = Path.GetDirectoryName(Path.GetFullPath(destination))!;
        var staging = new DirectoryInfo(Path.Combine(parent, $".anim-import-{Guid.NewGuid():N}"));
        staging.Create();
        try
        {
            var stagedFile = Path.Combine(staging.FullName, Path.GetFileName(destination));
            if (File.Exists(destination))
            {
                File.Copy(destination, stagedFile);
            }
            if (!await importAndValidate(staging, stagedFile))
            {
                return false;
            }
            File.Move(stagedFile, destination, true);
            return true;
        }
        finally
        {
            // Only remove the unique directory created by this invocation.
            staging.Delete(true);
        }
    }
}
